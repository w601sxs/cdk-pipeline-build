#!/usr/bin/env python3

from aws_cdk import core

from cdk_pipeline_build.cdk_pipeline_build_stack import CdkPipelineBuildStack


app = core.App()
CdkPipelineBuildStack(app, "cdk-pipeline-build")

app.synth()
