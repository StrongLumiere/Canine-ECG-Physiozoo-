import matplotlib.pyplot as plt

def save(grid_d, grid_x, grid_y, save_path, id, seg_num, image_size=(224, 224)):
    """
    Save a polar-transformed spectrogram as a high-resolution PNG image with a transparent background.

    Parameters:
    - grid_d (2D array): The spectrogram data in polar coordinates (intensity values).
    - grid_x (2D array): X-coordinates of the spectrogram in Cartesian space.
    - grid_y (2D array): Y-coordinates of the spectrogram in Cartesian space.
    - save_path (str): The directory where the image will be saved.
    - id (str): Identifier for the file name (used to create the final file name).
    - image_size (tuple): Desired image size in pixels (width, height). Default is (224, 224).
    
    Steps:
    -    # Step 1 : Set figure size
    -    # Step 2 : Reshape image
    -    # Step 3 : Display image & Get rid of background and axis
    -    # Step 4 : Save the image as .png
    
    """
    
    # step1: Set figure size to create a high-resolution output
    figure_size = (6, 6)  # Unused but could be customized for larger images
    dpi = 1000  # Set DPI to 1000 for high resolution (ensures clear image even at 224x224 pixels)
    fig_size_inch = (image_size[0] / dpi, image_size[1] / dpi)  # Convert pixel dimensions to inches for plt.subplots
    
    # Create a figure and axis with the specified size and resolution
    fig, ax = plt.subplots(figsize=fig_size_inch, dpi=dpi)
    
    # step2: Reshape grid_x and grid_y to match the dimensions of grid_d if necessary
    grid_x = grid_x.reshape(grid_d.shape)
    grid_y = grid_y.reshape(grid_d.shape)
    
    # Set the extent of the image based on the min and max of grid_x and grid_y
    extent = [grid_x.min(), grid_x.max(), grid_y.min(), grid_y.max()]
    
    # step3: Display the spectrogram data as an image and erase the background and axis
    # - 'extent' specifies the bounding box of the image in data coordinates
    # - 'origin' set to 'lower' means the [0,0] coordinate is at the bottom-left corner
    # - 'cmap' specifies the color map to use for intensity visualization (jet color map)
    # - 'aspect' set to 'auto' allows for automatic aspect ratio adjustment

    ax.imshow(grid_d, extent=extent, origin='lower', cmap='jet', aspect='auto')
    
    # Remove axis lines, labels, and ticks for a clean image
    ax.axis('off')  # Hide the entire axis (frame, ticks, and labels)
    
    # Ensure there is no padding and no border around the image
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    ax.margins(0, 0)  # Set margins to 0 to eliminate white borders
    ax.xaxis.set_major_locator(plt.NullLocator())  # Remove x-axis ticks
    ax.yaxis.set_major_locator(plt.NullLocator())  # Remove y-axis ticks
    
    # step4: Save the figure as a PNG image
    # - 'format' set to 'png' for lossless quality
    # - 'transparent=True' to make the background transparent
    # - 'bbox_inches' set to 'tight' to fit the image tightly around data
    # - 'pad_inches=0' removes extra padding around the saved image
    plt.savefig(f'{save_path}\\{id}-segment{seg_num}.png', format='png', transparent=True, bbox_inches='tight', pad_inches=0)
    
    # Close the figure to free memory
    plt.close()