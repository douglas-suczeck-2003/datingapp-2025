import { Component, inject, Input, input, signal } from '@angular/core';
import { Register } from "../account/register/register";
import { User } from '../../types/user';
import { Router, RouterLink } from "@angular/router";

@Component({
  selector: 'app-home',
  imports: [Register, RouterLink],
  templateUrl: './home.html',
  styleUrl: './home.css'
})
export class Home {
  protected registerMode = signal(false);
  router = inject(Router)

  showRegister(value: boolean) {
    this.registerMode.set(value);
  }

  openLearnMore() {
    this.router.navigateByUrl('/blank')
  }
}
