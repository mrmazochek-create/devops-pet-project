.PHONY: build push clean

# Собрать Docker образ локально
build:
	docker build -t devops-app:latest ./app

# Запустить локально
run:
	docker run -p 8080:8080 --name devops-test devops-app:latest

# Остановить и удалить контейнер
stop:
	docker stop devops-test || true
	docker rm devops-test || true

# Очистить образы
clean:
	docker rmi devops-app:latest || true

# Показать логи
logs:
	docker logs -f devops-test
