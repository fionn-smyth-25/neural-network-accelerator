`timescale 1ns / 1ps

module convolver
#(parameter K = 3, //kernal is size K x K
  parameter N = 5,
  parameter DATA_WIDTH = 64) //input matrix is size N x N
(
    input clk, rst, en,
    input[DATA_WIDTH-1:0] activation,
    input[DATA_WIDTH-1:0] weights_flat[(K*K)-1:0], //array of K*K weights
    output[DATA_WIDTH-1:0] conv_out
);

    wire[DATA_WIDTH-1:0] out[(K*K)-1:0]; //individual MAC outputs
    wire[DATA_WIDTH-1:0] shift_out[K-1:0]; //shift reg outputs

    // index = aij
    // a11 a12 a13
    // a21 a22 a23
    // a31 a32 a33

    generate 
        genvar i, j; //i = rows, j = columns
        for (i = 0; i < K; i++) begin
            for (j = 0; j < K; j++) begin
            
                localparam idx = (i * K) + j; 
                
                if (i == 0 && j == 0) begin //top left corner
                    mac MAC_INST (clk, rst, en, activation, weights_flat[idx], 0, out[idx]);
                end 
                else if (j == 0) begin //in the first column, all MACs will have input from a shift register
                    shift_register SHIFT_REG_INST (clk, rst, en, 1'b1, out[idx][DATA_WIDTH-1], shift_out[i]);
                    mac MAC_INST (clk, rst, en, activation, weights_flat[idx], out[idx-1], out[idx]);       
                end        
                else if (i == K && j == K) begin //bottom right corner
                    mac MAC_INST (clk, rst, en, activation, weights_flat[idx], out[idx-1], conv_out);      
                end      
                
                //default
                mac MAC_INST (clk, rst, en, activation, weights_flat[idx], out[idx-1], out[idx]);   
                 
            end
        end
    endgenerate 
    
endmodule
