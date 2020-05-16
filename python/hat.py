def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)

have_hat = hat_available('green')
print('hat available is', have_hat)
