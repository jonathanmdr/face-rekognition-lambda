import boto3
import json

s3 = boto3.resource('s3')
client = boto3.client('rekognition')


def detect_faces():
    detected_faces = client.index_faces(
        CollectionId='faces',
        DetectionAttributes=['DEFAULT'],
        ExternalImageId='TEMPORARY_FILE_TO_COMPARISON',
        Image={
            'S3Object': {
                'Bucket': 'jhmede-fa-images',
                'Name': '_analyze.jpg'
            }
        }
    )
    return detected_faces


def create_detected_face_id_list(faces):
    detected_face_ids = []
    for image in range(len(faces['FaceRecords'])):
        detected_face_ids.append(faces['FaceRecords'][image]['Face']['FaceId'])
    return detected_face_ids


def compare_images(detected_face_ids):
    result_comparison = []
    for identifier in detected_face_ids:
        result_comparison.append(
            client.search_faces(
                CollectionId='faces',
                FaceId=identifier,
                FaceMatchThreshold=80,
                MaxFaces=10
            )
        )
    return result_comparison


def generate_json_data(comparison_result):
    json_data = []
    for face_recognized in comparison_result:
        if (len(face_recognized.get('FaceMatches'))) >= 1:
            person = dict(
                name=face_recognized['FaceMatches'][0]['Face']['ExternalImageId'],
                similarity=round(face_recognized['FaceMatches'][0]['Similarity'], 2)
            )
            json_data.append(person)
    return json_data


def send_response_file_to_s3_bucket(response):
    file = s3.Object('jhmede-fa-site', 'data.json')
    file.put(Body=json.dumps(response))


def remove_image_used_by_comparison(face_ids):
    client.delete_faces(
        CollectionId='faces',
        FaceIds=face_ids
    )


def main(event, context):
    detected_faces = detect_faces()
    face_ids = create_detected_face_id_list(detected_faces)
    comparison_result = compare_images(face_ids)
    data = generate_json_data(comparison_result)
    send_response_file_to_s3_bucket(data)
    remove_image_used_by_comparison(face_ids)
    print(json.dumps(data, indent=4))
