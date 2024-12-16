# Collect arguments
args = ARGV.map(&:to_i) # Convert to integers
# Sort the array
sorted_args = args.sort
# Print the sorted numbers
sorted_args.each { |arg| puts arg }

