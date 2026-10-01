import matplotlib.pyplot as plt

def plot_polar_ecg(id, k, x, y, reversed):

    cm= 'jet'

    # K-Space plot
    fig, ax = plt.subplots(figsize=(6, 6))

    # polar stft - Reversed
    extent1 = [x.min(), x.max(), y.min(), y.max()]

    cax1 = ax.imshow(
        k,
        extent=extent1,
        origin='lower',
        cmap=cm,
        aspect='auto'
    )
    ax.axis('off')

    if reversed:
        ax.set_title(f'Grid of Original {id} - Reversed')
       
    else:
        ax.set_title(f'Grid of Original {id}')
           
    plt.show()

    return
