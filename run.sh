
cd /srv/

# test
export GRADIO_DEBUG=1

gradio gradio_link.py 2>&1 | tee run.log
