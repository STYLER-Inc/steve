install:
	@echo "# Installing"

	@# Run install script
	./setup/install.bash

	@echo "# sprofs installation complete!"
	exit 0

uninstall:
	@echo "# Uninstalling sprofs..."
	rm -rf "$(HOME)/.sprofs"
