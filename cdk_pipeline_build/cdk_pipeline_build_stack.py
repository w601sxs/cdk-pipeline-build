from aws_cdk.core import Stack, StackProps, Construct, SecretValue
from aws_cdk.pipelines import CdkPipeline, SimpleSynthAction
import aws_cdk.aws_s3 as _s3

import aws_cdk.aws_codepipeline as codepipeline
import aws_cdk.aws_codepipeline_actions as codepipeline_actions

class CdkPipelineBuildStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()
        bucket = _s3.Bucket(self, 'bucket')

        pipeline = CdkPipeline(self, "Pipeline",
            pipeline_name = "MyAppPipeline",
            cloud_assembly_artifact = cloud_assembly_artifact,
            source_action = codepipeline_actions.S3SourceAction(
                bucket = bucket.bucket_name,
                bucket_key = "faropt-master.zip",
                action_name = "S3",
                output = source_artifact),
            synth_action = SimpleSynthAction.standard_npm_synth(
                source_artifact = source_artifact,
                cloud_assembly_artifact = cloud_assembly_artifact,
                build_command = "cdk synth")
        )
