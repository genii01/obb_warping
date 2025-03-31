.PHONY: run clean

# Default target
all: run

# Run the image warping script
run:
	python image_warping.py

# Clean up generated files
clean:
	rm -f original_with_points.jpg warped_result.jpg

# Install required dependencies
install:
	pip install opencv-python numpy matplotlib

# Help target
help:
	@echo "Available targets:"
	@echo "  make run     - Run the image warping script"
	@echo "  make clean   - Remove generated files"
	@echo "  make install - Install required dependencies"
	@echo "  make help    - Show this help message" 