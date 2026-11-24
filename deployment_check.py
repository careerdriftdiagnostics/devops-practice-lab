def deployment_allowed(environment, checks_passed):
    """A simulated decision only. This performs no deployment."""
    return environment == "lab" and checks_passed is True
