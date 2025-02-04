OK_FORMAT = True

test = {
    "name": "Q1.1a Implement VAE",
    "points": 15,
    "suites": [
        {
            "cases": [
                {
                    "code": """
                    >>> sum(p.numel() for p in model.parameters() if p.requires_grad) < 1000000
                    True
                    """,
                    "failure_message": "Model has too many trainable parameters",
                    "hidden": False,
                    "locked": False,
                    "points": 0,
                    "success_message": "Parameter count test passed",
                },
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest",
        }
    ],
}
