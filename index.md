<html lang="en">
  <head>
    <meta charset="utf-8"><!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    
    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    
    <!-- Popper JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    
    <!-- Latest compiled JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>

  </head>
  <body>
    <nav class="navbar navbar-expand-sm bg-primary navbar-dark">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">Credit Scoring using FICO additive formula</a>
          </li>

        </ul>
      </nav>
      <br>
      <div class="container">
        <div class="card">
          <div class="card-header">User Information</div>
          <div class="card-body">
            <form action="/action_page.php">
            <div class="form-group">
              <label for="email">Number of recharge:</label>
              <input type="number" class="form-control" placeholder="" id="number_of_recharge">
            </div>
            <div class="form-group">
              <label for="pwd">Age of sim:</label>
              <input type="number" class="form-control" placeholder="" id="age_of_sim">
            </div>
            <div class="form-group">
              <label for="pwd">Balance before recharge:</label>
              <input type="number" class="form-control" placeholder="" id="balance_before_recharge">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form></div>
          <div class="card-footer">Credit Score: 0</div>
        </div>
      </div>
  </body>
</html>