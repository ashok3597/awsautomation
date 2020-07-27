# coding: utf-8

import boto3
session =  boto3.Session(profile_name="automation")
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
as_client.describe_policies()
as_client.execution_policy(AutoScalingGroupName='Notifion Example group', PolicyName = 'Scale Down')
as_client.execution_policy(AutoScalingGroupName='Notifion Example group', PolicyName = 'Scale Up')
