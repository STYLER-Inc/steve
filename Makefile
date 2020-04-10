install:
	@echo "# Installing"

	@# Run install script
	./setup/install.bash

	@echo "# steve installation complete!"
	exit 0

uninstall:
	@echo "# Uninstalling steve..."
	rm -rf "$(HOME)/.steve"
