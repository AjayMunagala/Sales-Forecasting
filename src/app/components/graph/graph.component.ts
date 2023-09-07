import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-graph',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.css']
})
export class GraphComponent implements OnInit {
  actualGraphImageUrl: string | undefined;
  predictedGraphImageUrl: string | undefined;
  forecastGraphImageUrl: string | undefined;
  combinedGraphImageUrl: string | undefined;
  
  mse: number | undefined;
  rmse: number | undefined;
  mape: number | undefined;
  accuracy: number | undefined;
  predictedPrice: number | undefined;

  constructor(private router: Router) { }

  ngOnInit() {
    const state = window.history.state;
    this.actualGraphImageUrl = state.actualGraphImageUrl;
    this.predictedGraphImageUrl = state.predictedGraphImageUrl;
    this.forecastGraphImageUrl = state.forecastGraphImageUrl;
    this.combinedGraphImageUrl = state.combinedGraphImageUrl;
    
    this.mse = state.mse;
    this.rmse = state.rmse;
    this.mape = state.mape;
    this.accuracy = state.accuracy;
    this.predictedPrice = state.predictedPrice;
  }

  navigateToResults() {
    this.router.navigate(['/results'], {
      state: {
        mse: this.mse,
        rmse: this.rmse,
        mape: this.mape,
        accuracy: this.accuracy,
        predictedPrice: this.predictedPrice
      }
    });
  }
}
