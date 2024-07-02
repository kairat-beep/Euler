use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let f = BufReader::new(File::open("11.txt").unwrap());
    let matrix: Vec<Vec<i32>> = f.lines()
        .map(|l| l.unwrap().split(char::is_whitespace)
             .map(|number| number.parse().unwrap())
             .collect())
        .collect();
    let rows = 20;
    let cols = 20;
    let mut max:i32 = 0;
    for i in 0..rows{
        for j in 0..cols{
            if i>=3 && j>=3{
                let mult_diag_up = matrix[i][j]* matrix[i-1][j-1]* matrix[i-2][j-2]* matrix[i-3][j-3];                 
                if mult_diag_up>max {
                    max=mult_diag_up;
                }
                if i<cols-3 && j<rows-3{
                    let mult_diag_down= matrix[i][j]* matrix[i-1][j+1]* matrix[i-2][j+2]* matrix[i-3][j+3];                 
                    if mult_diag_down>max {
                        max=mult_diag_down;
                    }
                }
            }
            if j>=3{
                let mult_horiz = matrix[i][j]* matrix[i][j-1]* matrix[i][j-2]* matrix[i][j-3];                 
                if mult_horiz > max {
                    max = mult_horiz;
                }
            }
            if i>=3{
                let mult_vertic= matrix[i][j]* matrix[i-1][j]* matrix[i-2][j]* matrix[i-3][j];                 
                if mult_vertic > max {
                    max=mult_vertic;
                }
            }
        }
    }
    println!("{}",max);
}

