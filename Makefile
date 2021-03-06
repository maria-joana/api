#####################################################
# Makefile containing shortcut commands for project #
#####################################################

# MACOS USERS:
#  Make should be installed with XCode dev tools.
#  If not, run `xcode-select --install` in Terminal to install.

# WINDOWS USERS:
#  1. Install Chocolately package manager: https://chocolatey.org/
#  2. Open Command Prompt in administrator mode
#  3. Run `choco install make`
#  4. Restart all Git Bash/Terminal windows.

.PHONY: docker-clean docker-down docker-force docker-logs docker-start docker-stop docker-up

docker-clean:
	docker-compose down --rmi all --volumes

docker-down:
	docker-compose down --remove-orphans

docker-force:
	docker-compose up --force-recreate

docker-logs:
	docker-compose logs -f

docker-start:
	docker-compose start

docker-stop:
	docker-compose stop

docker-up:
	docker-compose up

.PHONE: django-csu django-m django-mm django-testf8

django-csu:
	docker-compose run --rm api sh -c 'python manage.py createsuperuser --email admin@mariajoana.com.br'

django-m:
	docker-compose run --rm api sh -c 'python manage.py migrate'

django-mm:
	docker-compose run --rm api sh -c 'python manage.py makemigrations'

django-testf8:
	docker-compose run --rm api sh -c 'python manage.py test && flake8'
