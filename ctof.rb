puts "Enter the temperature in C/F to be converted"
temp = gets.chomp

if temp =~ /^([+-]?[0-9]+)([CF])$/
  input_num = $1
  input_type = $2


  if input_type.eql? "C"
    celcius = input_num.to_f
    farenheit = (celcius * 9 / 5) + 32
  else
    farenheit = input_num.to_f
    celcius = (farenheit - 32) * 5 / 9
  end
  
  puts "Temperature in celcius: "+celcius.to_s+"C"
  puts "Temperature in farenhiet: "+farenheit.to_s+"F"
else
  puts "Expected a temperature input like 40C or 104F. But got "+"'"+temp+"\'"
end  