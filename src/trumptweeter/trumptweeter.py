import docker 
from itertools import dropwhile
import hashlib 

def parse_model_output(string, seed):
    outraw_l = string.split('\t\n')[-1].replace('\n', ' ').replace(seed, '')
    def is_nonsense(string):
        whitelist = {'AMERICA', 'GREAT', 'MAKE', 'AGAIN'}
        return string not in whitelist and string.upper() == string
    def skip_upper(string):
        return ' '.join( dropwhile(is_nonsense, string.split() ))
    return skip_upper(outraw_l)

def fetch_tweet(primetext, seed = None, temperature=0.4):
    """
    if seed is given, it overrides primetext. Otherwise a seed is calculated from the primetext.
    """
    REPO_URL = "perhogfeldt/trumptweeter:latest"
    client = docker.from_env()
    container = None
    model = "cv/lm_lstm_epoch46.57_1.3843.t7"
    print(model)
    if not seed:
        seed = hashlib.md5(primetext.encode()).hexdigest()
    print(seed)
    try:
        container = client.containers.run(
                REPO_URL,
                f"{model} -primetext '{seed}' -temperature {temperature} -length 280",
                detach=True,
        )
        result = container.wait()
        stdout = container.logs().decode("utf-8")
    finally:
        if container is not None:
            container.remove()
    return parse_model_output(stdout, seed)
