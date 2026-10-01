import numpy as np
from scipy.interpolate import griddata

def spectrogram_polar_transform(d, grid_resolution='auto', flipped_up=True, method='linear'):
    """
    Transforms a spectrogram to a polar representation using interpolation.

    Parameters:
    - d (2D array): The input spectrogram to be transformed.
    - grid_resolution (str or int): The resolution of the output grid.
        - 'auto' (default): Automatically calculates resolution based on input size.
        - int: Specifies the number of grid points along each dimension.
    - flipped_up (bool): If True, flips the input spectrogram vertically (up-down).
    - method (str): Interpolation method used in griddata (e.g., 'linear', 'cubic').

    
    Steps:
    -    # Step1 : Cartesian coordinate setting
    -    # Step2 : Polar mapping
    -    # Step 3: Interpolation

    Returns:
    - grid_d (2D array): The polar-transformed spectrogram data.
    - grid_x (2D array): X-coordinates of the grid in Cartesian space.
    - grid_y (2D array): Y-coordinates of the grid in Cartesian space.
    """
    nx, ny = d.shape  # Get the number of rows (nx) and columns (ny) in the input spectrogram

    # Step 1: Cartesian coordinate setting #
    radii = np.linspace(0, 1, nx)  # Radial coordinates from 0 to 1 for each row (scale)
    theta = np.linspace(0, 2 * np.pi, ny)  # Angular coordinates from 0 to 2π for each column (time)
    kx_list, ky_list = [], []
    

    #Step 2: Polar mapping: Convert polar coordinates to Cartesian (kx, ky) for each radius #
    for r in radii:
        kx = r * np.cos(theta)  # X-coordinate
        ky = r * np.sin(theta)  # Y-coordinate
        kx_list.append(kx)
        ky_list.append(ky)

    # Combine lists to form full Cartesian coordinate arrays
    kx = np.concatenate(kx_list)
    ky = np.concatenate(ky_list)
    k = kx + 1j * ky  # Complex representation, if needed (not used in further steps)
    kx, ky = np.real(k), np.imag(k)  # Real and imaginary parts

    # Flip the spectrogram vertically if required
    if flipped_up:
        d = np.flipud(d)  # Flip the spectrogram data along the vertical axis

        

    # Step 3: Interpolation - Determine grid resolution and map to Cartesian grid
    if grid_resolution == 'auto':
        # Calculate the resolution automatically based on data points in polar k-space
        ndata_points = k.size  # Total number of polar k-space data points
        radius = np.sqrt(ndata_points / np.pi)  # Estimated radius based on data point density
        diameter = 2 * radius  # Diameter to cover the full grid
        n = int(diameter)  # Set resolution to diameter
    elif isinstance(grid_resolution, int):
        n = grid_resolution  # Set resolution directly if specified as an integer
    else:
        raise ValueError("grid_resolution must be 'auto' or an integer.")

    # Flatten the spectrogram and coordinates for interpolation
    d = np.asarray(d).flatten()  # Flatten the spectrogram data to 1D array for interpolation
    kx = np.asarray(kx).flatten()  # Flatten the x-coordinates
    ky = np.asarray(ky).flatten()  # Flatten the y-coordinates
    
    # Generate a mesh grid in Cartesian space with specified resolution
    grid_x, grid_y = np.mgrid[min(kx):max(kx):complex(n), min(ky):max(ky):complex(n)]
    
    # Perform interpolation to map polar data to the Cartesian grid
    grid_d = griddata(points=np.column_stack((kx, ky)), values=d, xi=(grid_x, grid_y), method=method)

    return grid_d, grid_x, grid_y
