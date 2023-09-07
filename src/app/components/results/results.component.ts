import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {
  mse: number | undefined;
  rmse: number | undefined;
  mape: number | undefined;
  accuracy: number | undefined;
  predictedPrice: number | undefined;

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    const state = window.history.state;
    this.mse = state.mse;
    this.rmse = state.rmse;
    this.mape = state.mape;
    this.accuracy = state.accuracy;
    this.predictedPrice = state.predictedPrice;
  }
}
