`timescale 1ns / 1ps

module convolver
#(parameter K = 3, //kernal is size K x K
  parameter N = 5,
  parameter DATA_WIDTH = 64) //input matrix is size N x N
(
    input clk, rst, en,
    input[DATA_WIDTH-1:0] activation,
    input[DATA_WIDTH-1:0] weights_flat[(K*K)-1:0] //array of K*K weights
);

    wire[DATA_WIDTH-1:0] temp_outs[(K*K)-1:0];
    wire shift_out[K-1:0]; //outputs from shift registers

    generate 
        genvar i, j;
        for (i = 0; i < K; i++) begin
            for (j = 0; j < K; j++) begin
            
                localparam idx = (i * K) + j; 
                
                if (i == 0 && j == 0) begin //top left corner
                    mac MAC_INST (clk, rst, en, activation, weights_flat[idx], 0, temp_outs[idx]);
                end
                else if (i == 0 && j == K) begin //top right corner
                    shift_register SHIFT_REG_INST (clk, rst, en, 1'b1, weights_flat[idx][DATA_WIDTH-1], shift_out[1]);
                end        
                else if (i == K && j == 0) begin //bottom left corner  
                end        
                else if (i == K && j == K) begin //bottom right corner
                end        
               
                
            end
        end
    endgenerate 
    
endmodule
