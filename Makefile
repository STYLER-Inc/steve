install:
	@echo "# Installing"

	@# Run install script
	./setup/install.bash

	@echo "# profs installation complete!"
	exit 0

uninstall:
	@echo "# Uninstalling profs..."
	rm -rf "$(HOME)/.profs"
