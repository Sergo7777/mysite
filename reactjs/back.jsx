import React from "react";
import ReactDOM from "react-dom";



const title = (
    <div style={{"height" : "10%"}} className="container-top">
        <h1 className="col-lg-8"> 
            Reservation of tables for the date 
        </h1>
    </div>
);

const datepicker = (
    <div class="col-md-2" className="datepicker">
        <h3 class="calendar">Select the date: </h3> 
        <input type="text" class="input" id="datepicker" value="" />
    </div>
)

const footer = (
    <div className="footer">
        <div className="col-lg-6 no-margin">
            <a href='/'> 2017 © Reservation </a><span> все права защищены </span>
        </div>
    </div>
);



var Title = React.createClass({
    render: function(){
        return(
            title
        )
    }
});

var TableList = React.createClass({
    loadTableFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },
    componentDidMount: function() {
        this.loadTableFromServer();
        setInterval(this.loadTableFromServer, 
                    this.props.pollInterval)
    }, 
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var table = this.state.data.map(function(table){
                return 
                    <li> {table.name} </li>
            })
        }
        return (
            <ul>
                {table}
            </ul>
        )
    }
})
var ContentList = React.createClass({
    render: function() {
        return(
            <div style={{"width" : "100%", "height" : "500px", "background-color": "lightseagreen",
                    "border": "1px solid #fff", "border-radius": "20px"}} className="container">
                <TableList url='/api/table'/>   
            </div>
        )
    }
});
var Content = React.createClass({
    render: function() {
        return(
                datepicker,
                <ContentList />
            )        
    }
})

var Footer = React.createClass({
    render: function(){
        return(
            footer
        )
    }
});


var App = React.createClass({
    render: function()  {
        return  (
            <div className="App">
                <div style={{"width" : "100%", "height" : "600px", "background-color": "mediumslateblue",
    "border": "1px solid #fff", "padding-right": "10px"}} className="container-one">
                    <Title />
                    <Content />    
                </div>
                <Footer />
            </div>
        );
    }
});

ReactDOM.render(
    <App />,
    document.getElementById('root')
);
