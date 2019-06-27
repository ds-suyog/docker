import docker
client = docker.from_env()

for image in client.images.list():
  print(image)
  #print(image.id)

for container in client.containers.list():
  print(container.id)

# create docker image from Dockerfile
try:
	#image = client.images.build(path='/home/suyog/github/docker/')
	image = client.images.build(path="./", tag={'sks-docker-flask-app'})
	client.containers.run({"sks-docker-flask-app"}, name={"sks-docker-container"}, detach=True)
	print(image)
except RuntimeError as e:
	print(e)

#client.containers.run({'sks-docker-flask-app'}, name={'sks-docker-container'}, detach=True)

print()
for image in client.images.list():
  print(image)
