# coding: utf-8
import boto3

session = boto3.Session(profile_name = 'automation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = 'key' + '.pem'
key = ec2.create_key_pair(keyName = 'key_name')
key.key_material
with open(key_path, "w") as key_file:
    key_file.write(key.key_material)

get_ipython().run_line_magic("ls", '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IUSR, stat.S_WUSR)
get_ipython().run_line_magic("ls", '-l python_automation_key.pem')
ec2.images.filter(Owners =['amazon'])
list(ec2.images.filter(Owners =['amazon']))
len(list(ec2.images.filter(Owners =['amazon']))
img = ec2.Image('') #choose your AMI Id from the region you want from the AWS console)
img.name
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2 = ec2_apse2.Imave('') ##choose your AMI Id from the region you want from the AWS console)
img_apse2.name
img.name
ami_name ='' #depends on the ami we choose
filters = [{'Name':'name', 'Values':[ami_name]}]
list(ec2.images.filter(Owners =['amazon'], Filters = filters))
list(ec2_apse2.images.filter(Owners =['amazon'], Filters = filters))
img
key
instances=ec2.create_instances(imageId=img.id, MinCount = 1, MaxCount = 1, instanceType = 't2.micro', KeyName=key_name)
instances
ec2.instances(id='') #instanceId of choice
inst = instances[0]
inst.terminate()
instances=ec2.create_instances(imageId=img.id, MinCount = 1, MaxCount = 1, instanceType = 't2.micro', KeyName=key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups #Authorizing the port SSH for Instance access
sg  = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort':22,'ToPort':22,'IpProtocol':'TCP','IpRanges':[{'CidrIp':' '}]}])#our Ip address range here
sg.authorize_ingress(IpPermissions=[{'FromPort':80,'ToPort':80,'IpProtocol':'TCP','IpRanges':[{'CidrIp':'0.0.0.0/0'}]}])
inst.public_dns_name
get_ipython().run_line_magic('history', '')
