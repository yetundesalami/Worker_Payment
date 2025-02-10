generate_workers <- function(num = 400) {
  # Dynamically generates a list of worker data frames
  set.seed(123)  # Ensures reproducibility
  workers <- data.frame(
    ID = 1:num,
    Name = paste0("Worker_", 1:num),
    Salary = sample(5000:35000, num, replace = TRUE),
    Gender = sample(c("Male", "Female"), num, replace = TRUE)
  )
  return(workers)
}

determine_employee_level <- function(worker_df) {
  # Determines employee level based on salary and gender conditions
  worker_df$Employee_Level <- "N/A"
  
  worker_df$Employee_Level[worker_df$Salary > 10000 & worker_df$Salary < 20000] <- "A1"
  worker_df$Employee_Level[worker_df$Salary > 7500 & worker_df$Salary < 30000 & worker_df$Gender == "Female"] <- "A5-F"
  
  return(worker_df)
}

generate_payment_slips <- function(workers) {
  # Prints payment details for each worker
  cat("\nPayment Slips:\n")
  print(workers)
}

# Main Execution
workers <- generate_workers()
workers <- determine_employee_level(workers)
generate_payment_slips(workers)
