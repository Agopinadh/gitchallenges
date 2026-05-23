import boto3

# Create EC2 client
ec2 = boto3.resource('ec2', region_name='ap-south-1')

# Create EC2 instance
instances = ec2.create_instances(
    ImageId='ami-0f5ee92e2d63afc18',  # Example Amazon Linux AMI
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-keypair-name'
)

print("EC2 Instance Created!")
print("Instance ID:", instances[0].id)
