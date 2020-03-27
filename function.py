import boto3
ec2=boto3.resource('ec2')
#create vpc
ip=input('Enter the CIDRBLOCK ip address : ')
vpc=ec2.create_vpc(ip)

