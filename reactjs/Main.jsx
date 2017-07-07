import React from "react";
import ReactDOM from "react-dom";

var TablesList = React.createClass({
    loadTablesFromServer: function(){
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
        this.loadTablesFromServer();
        setInterval(this.loadTablesFromServer, 
                    this.props.pollInterval)
    }, 
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var tablelists = this.state.data.map(function(){
                return <li> {table.id} </li>
            })
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {tablelists}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<TablesList url='/api/table' pollInterval={1000} />, 
    document.getElementById('root'))
