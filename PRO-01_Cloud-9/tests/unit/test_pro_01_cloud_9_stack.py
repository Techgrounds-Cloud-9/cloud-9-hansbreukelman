import aws_cdk as core
import aws_cdk.assertions as assertions
from pro_01_cloud_9.pro_01_cloud_9_stack import Pro01Cloud9Stack


def test_sqs_queue_created():
    app = core.App()
    stack = Pro01Cloud9Stack(app, "pro-01-cloud-9")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = Pro01Cloud9Stack(app, "pro-01-cloud-9")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
