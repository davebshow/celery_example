# celery_example


## Get RabbitMQ going

You may need to install Erlang if you don't have it::

```
# Check if installed
$ which erl

# If not installed

$ wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
$ sudo dpkg -i erlang-solutions_1.0_all.deb
$ sudo apt-get update
$ sudo apt-get install erlang
```

Get RabbitMQ dist:

```
$ cd
$ wget https://github.com/rabbitmq/rabbitmq-server/releases/download/rabbitmq_v3_6_12/rabbitmq-server-generic-unix-3.6.12.tar.xz
```

Fire it up:
```
$ tar xf rabbitmq-server-generic-unix-3.6.12.tar.xz
$ cd rabbitmq_server-3.6.12/
sbin/rabbitmq-server
```

Clone this repo:
```
git clone https://github.com/davebshow/celery_example.git
```

Install Celery:
```
$ pip install celery
```

Run the Celery task queue:

```
$ cd celery_example
& celery -A tasks worker --loglevel=info
```

Fire up a new terminal and run the example:

```
cd celery_example
python run.py
```


