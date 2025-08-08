.PHONY: install setup run clean help

# Kolory dla czytelności
GREEN=\033[0;32m
YELLOW=\033[1;33m
RED=\033[0;31m
NC=\033[0m # No Color

help: ## Pokaż dostępne komendy
	@echo "🤖 OttoNinjaServoDriver - Dostępne komendy:"
	@echo "=========================================="
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(GREEN)%-10s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Kompletna instalacja (venv + dependencies + konfiguracja IP)
	@echo "$(YELLOW)🤖 Instalacja OttoNinjaServoDriver...$(NC)"
	@$(MAKE) setup
	@$(MAKE) config
	@echo "$(GREEN)✅ Instalacja zakończona!$(NC)"
	@echo "$(YELLOW)Uruchom: make run$(NC)"

setup: ## Utwórz venv i zainstaluj dependencies
	@echo "$(YELLOW)📦 Tworzenie środowiska wirtualnego...$(NC)"
	python3 -m venv venv
	@echo "$(YELLOW)📚 Instalowanie zależności...$(NC)"
	./venv/bin/pip install -r requirements.txt

config: ## Skonfiguruj adres IP ESP8266
	@echo "$(YELLOW)🌐 Konfiguracja adresu IP ESP8266...$(NC)"
	@read -p "Podaj adres IP Wemos D1 Mini: " esp_ip; \
	sed -i.bak "s/ESP8266_IP = .*/ESP8266_IP = '$$esp_ip'/" servo.py; \
	echo "$(GREEN)⚙️  IP zaktualizowany: $$esp_ip$(NC)"

run: ## Uruchom aplikację
	@echo "$(YELLOW)🚀 Uruchamianie aplikacji...$(NC)"
	@echo "$(YELLOW)📱 Otwórz: http://127.0.0.1:5000$(NC)"
	./venv/bin/python app.py

clean: ## Wyczyść pliki instalacyjne
	@echo "$(YELLOW)🧹 Czyszczenie...$(NC)"
	rm -rf venv
	rm -f servo.py.bak

dev: setup ## Szybka instalacja dla developera (bez pytania o IP)
	@echo "$(GREEN)✅ Środowisko deweloperskie gotowe!$(NC)"
	@echo "$(YELLOW)Ustaw IP ręcznie w servo.py, następnie: make run$(NC)"