import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';

@Component({
  selector: 'app-prediction',
  templateUrl: './prediction.component.html',
  styleUrls: ['./prediction.component.css']
})
export class PredictionComponent {
  file: File | undefined;
  periodicity: string | undefined;
  periodicNumber: number | undefined;
  showSpinner: boolean = false;

  constructor(
    private http: HttpClient,
    private router: Router,
    private spinner: NgxSpinnerService
  ) {}

  onSubmit(): void {
    if (this.file && this.periodicity && this.periodicNumber) {
      const formData = new FormData();
      formData.append('csvFile', this.file);
      formData.append('periodicity', this.periodicity);
      formData.append('periodicNumber', String(this.periodicNumber));

      
      this.spinner.show();

      this.http.post('http://localhost:5000/forecast', formData) 
        .subscribe(
          (response: any) => {
            console.log(response);
            this.spinner.hide();
          
            this.router.navigate(['/graph'], { state: response });
        

          },
          (error) => {
            console.error(error);
            this.spinner.hide();
            
          }
        );
    }
  }

  onFileChange(event: any): void {
    const fileList: FileList = event.target.files;
    if (fileList.length > 0) {
      this.file = fileList[0];
    }
  }
}
