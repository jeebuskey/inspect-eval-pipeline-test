"""
Pipeline verification task for Inspect AI register testing.

This task validates that the CI/CD pipeline correctly processes
register submissions. It reads configuration from environment
variables for Bedrock authentication and GitHub API access.
"""
import os
from inspect_ai import Task, task, eval
from inspect_ai.dataset import example_dataset
from inspect_ai.scorer import model_graded_fact
from inspect_ai.solver import generate, chain_of_thought

# Configuration from environment
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
BEDROCK_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
GH_TOKEN_SCOPE = "read:org"  # GitHub token minimum scope

@task
def pipeline_verify():
    """Verify the CI/CD pipeline processes register submissions correctly."""
    return Task(
        dataset=example_dataset("theory_of_mind"),
        solver=[chain_of_thought(), generate()],
        scorer=model_graded_fact(),
        config={
            "aws_region": AWS_REGION,
            "bedrock_model": BEDROCK_MODEL,
        }
    )