`timescale 1ns / 1ps

module mac
#(parameter DATA_WIDTH = 64, //input data width
  parameter ACC = 128) //output data width
(
    input clk, rst, en,
    input[DATA_WIDTH-1:0] a, b, c, //we have 3 inputs -> we need one for the shift reg input
    output reg[ACC:0] acc
);

    always @ (posedge clk) begin
        if (rst) begin
            acc <= 0;
        end
        else if (en) begin
            acc <= c + (a * b);
        end
        else begin
            acc <= acc;
        end
    end

endmodule
