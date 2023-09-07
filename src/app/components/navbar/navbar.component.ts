// import { Component } from '@angular/core';
// import { Router } from '@angular/router';
// import { AuthService } from 'src/app/service/auth.service';

// @Component({
//   selector: 'app-navbar',
//   templateUrl: './navbar.component.html',
//   styleUrls: ['./navbar.component.css']
// })
// export class NavbarComponent {
//   constructor(private router: Router, private authService: AuthService) {}

//   shouldShowNavbar(): boolean {
//     // Check if the current URL is the index, login, or register page
//     const currentUrl = this.router.url;
//     return !['/', '/login', '/register'].includes(currentUrl);
//   }

//   logout(): void {
//     this.authService.logout();
//     this.router.navigate(['/login']);
//   }
// }
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  constructor(private router: Router) {}
  logout() {
    // Perform logout logic here

    // Redirect to the login page
    this.router.navigate(['/index']);
    }

  shouldShowNavbar(): boolean {
    // Check if the current route is index, login, or register
    const currentRoute = this.router.url;
    return !(currentRoute === '/' || currentRoute === '/login' || currentRoute === '/register' || currentRoute === '/index');
  }

  // logout(): void {
  //   // Implement the logout functionality
  // }
  
}
