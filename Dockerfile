FROM nagadomi/torch7:latest

RUN git clone https://github.com/Hogfeldt/trumptweeter

WORKDIR /root/trumptweeter

ENTRYPOINT ["th", "sample.lua"]
