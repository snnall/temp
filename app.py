#!/usr/bin/env python3

from aws_cdk import core

from ae.ae_stack import AeStack


app = core.App()
AeStack(app, "ae", env={'region': 'us-east-1'})

app.synth()
