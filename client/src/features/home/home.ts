import { Component, inject, Input, input, signal } from '@angular/core';
import { Register } from "../account/register/register";
import { User } from '../../types/user';
import { Router, RouterLink } from "@angular/router";
import { AccountService } from '../../core/services/account-service';
import { ToastService } from '../../core/services/toast-service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-home',
  imports: [Register, RouterLink, FormsModule],
  templateUrl: './home.html',
  styleUrl: './home.css'
})
export class Home {
  protected registerMode = signal(false);
  protected accountService = inject(AccountService);
  router = inject(Router);
  private toast = inject(ToastService);
  protected loading = signal(false);
  protected guestCreds: any = {
    email: 'guest@test.com',
    password: 'Pa$$w0rd'
  };

  showRegister(value: boolean) {
    this.registerMode.set(value);
  }

  loginAsGuest() {
    this.loading.set(true);
    this.accountService.login(this.guestCreds).subscribe({
      next: () => {
        this.router.navigateByUrl('/members')
        this.toast.success('Logged in successfully')
        this.guestCreds = {};
      },
      error: error => {
        this.toast.error(error.error);
      },
      complete: () => this.loading.set(false)
    })
  }
}
