import docker 

def fetch_tweet(primetext, temperature=0.2):
    REPO_URL = "perhogfeldt/trumptweeter:latest"
    client = docker.from_env()
    container = None
    try:
        container = client.containers.run(
                REPO_URL,
                f"cv/lm_lstm_epoch8.99_1.5029.t7 -primetext {primetext} -temperature {temperature} -length 280",
                detach=True,
        )
        result = container.wait()
        stdout = container.logs().decode("utf-8")
    finally:
        if container is not None:
            container.remove()
    return stdout
