import { Component, inject } from '@angular/core';
import { Nav } from "../layout/nav/nav";
import { Router, RouterOutlet } from '@angular/router';
import { ConfirmDialogComponent } from "../shared/confirm-dialog/confirm-dialog.component";

@Component({
  selector: 'app-root',
  imports: [Nav, RouterOutlet, ConfirmDialogComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected router = inject(Router);
}
