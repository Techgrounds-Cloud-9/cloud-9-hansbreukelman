#!/usr/bin/env python3

import aws_cdk as cdk

from pro_01_cloud_9.pro_01_cloud_9_stack import Pro01Cloud9Stack


app = cdk.App()
Pro01Cloud9Stack(app, "pro-01-cloud-9")

app.synth()
