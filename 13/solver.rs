use std::fs::read_to_string;

fn add_big(l_op: &mut [u8],r_op:&String) {
   let mut index:usize= 51;
   let mut carry_bit = 0;

   for digit in r_op.chars().rev(){
        let digit:u8 = digit as u8 - 0x30; // get a digit form
        let sum = l_op[index] + digit + carry_bit;//look for carry bit
        l_op[index]=sum%10;
        carry_bit = sum /10;
        index-=1;
   }
   //keep iterating 100 50 digit numbers might carry 2 digits to the left of the original number
   if carry_bit == 1 {
        loop{
            let sum = l_op[index] + carry_bit;
            l_op[index]=sum%10;
            carry_bit = sum /10;
            if index == 0 ||carry_bit ==0 { 
                break;
            }
            index -= 1;
        }

   }
}

fn main(){
    let numbers:Vec<String> = read_to_string("50digNumbers.txt") 
            .unwrap()  // panic on possible file-reading errors
            .lines()  // split the string into an iterator of string slices
            .map(String::from)  // make each slice into a string
            .collect();  // gather them together into a vector   let contents:String = fs::read_to_string("50digNumbers.txt").expect("No file found");
    
    let mut accumulator:[u8;52]=[0;52];
    
    for number in numbers {
        add_big(& mut accumulator,&number);
    }

    let print_me: String = accumulator.iter().map(ToString::to_string).collect();
    println!("{print_me}");
}
