program ReverseNumber;
var
  num, rev, rem: integer;
begin
  write('Enter a number: ');
  readln(num);
  rev := 0;
  while num <> 0 do
  begin
    rem := num mod 10;
    rev := rev * 10 + rem;
    num := num div 10;
  end;
  writeln('Reversed Number: ', rev);
end.
