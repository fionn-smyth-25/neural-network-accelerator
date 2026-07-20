`timescale 1ns / 1ps

module shift_register
#(parameter N = 8) //register width
(
    input clk, rst, en,
    input direction, //enables shift left or shift right
    input data, //input bit
    output reg[N-1:0] out
);

    always @ (posedge clk) begin
        if (rst) begin
            out <= 0;
        end
        else if (en) begin //shift if enabled
            case (direction)
                1'b0: out <= {out[N-2:0], data}; //shift left
                1'b1: out <= {data, out[N-1:1]}; //shift right
            endcase
        end
        else begin //otherwise hold value
            out <= out;
        end
    end

endmodule
