# loads the weights into a .mem file for easy use later
# will probably get loaded into the BRAM of our NNA

from tensorflow import keras

model = keras.models.load_model("model.keras")

weights = model.get_weights() # get weights
fixed = (weights[0] * 256).astype(int) # convert to fixed point (for FPGA usage later)

with open("output_files/weights.mem","w") as f:
    for value in fixed.flatten():
        f.write(f"{value & 0xFFFF:04X}\n")
