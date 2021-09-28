let f x = x match | 1 => 10 | 2 => 20 | _ => 3;

let g x = x match
    | 1 => 10
    | n => 3 * n;
let h x => x match
    | 1 => 10 | _ => 4;

let f x = x match
    | x: Int => 1
    | y: Float => 2
    | _ => 0
;

let f p = p match
    | p: Person(age: Int, _) => age * 2
    | p: Worker(_, _, company) => len company
    ;