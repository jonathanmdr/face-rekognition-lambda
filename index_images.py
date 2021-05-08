import boto3

s3 = boto3.resource('s3')
client = boto3.client('rekognition')


def list_images():
    images = []
    bucket = s3.Bucket('jhmede-fa-images')
    for image in bucket.objects.all():
        images.append(image.key)
    return images


def index_images(images):
    for image in images:
        client.index_faces(
            CollectionId='faces',
            DetectionAttributes=[],
            ExternalImageId=image[:-4],
            Image={
                'S3Object': {
                    'Bucket': 'jhmede-fa-images',
                    'Name': image
                }
            }
        )


# client.create_collection(CollectionId='faces') -- Used to create a new collection on AWS Rekognition
result = list_images()
index_images(result)
