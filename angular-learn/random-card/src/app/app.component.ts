import { Component, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { UserService } from './services/user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'random-card';

  user: any; 
  constructor(
    private userService: UserService,
    private toastr: ToastrService,
    ){}

  ngOnInit(){
    this.userService.getUser().subscribe(
      (user: any) => {
        console.log(user);
        this.user = user.results[0];
      },
      (err) => {
        this.toastr.error(err.status, "Oops! Something is not right");
      }
    )
  }
}
